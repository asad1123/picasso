<script context="module">
  import { onMount } from "svelte";
  import Icon from "fa-svelte";
  import { faFilter, faSadTear } from "@fortawesome/free-solid-svg-icons";
  import ImageListItem from "./image-list-item.svelte";

  let menuIcon = faFilter;
  let notFoundIcon = faSadTear;
</script>

<script>
  let imageUrls;
  let nextPage = 1;
  let maxWidth = 1200;
  let prevWidth = 1200;
  let maxHeight = 1200;
  let prevHeight = 1200;
  let isLoading = false;

  function getImages() {
    let hostname = __API__
      ? __API__
      : `http://${window.location.hostname}:8000`;

    isLoading = true;
    fetch(
      `${hostname}/images/?page=${nextPage}&width=${maxWidth}&height=${maxHeight}`
    )
      .then(resp => resp.json())
      .then(function(data) {
        let imageMetadata = data.data;
        let requestPageInfo = data.page_info;
        nextPage = requestPageInfo.next_num;

        let newUrls = imageMetadata.map(
          image =>
            `https://picsum.photos/id/${image.id}/${image.width}/${image.height}`
        );

        imageUrls =
          imageUrls && imageUrls.length ? [...imageUrls, ...newUrls] : newUrls;

        isLoading = false;
        return false;
      });
  }

  function applyFilter() {
    if (prevHeight !== maxHeight || prevWidth !== maxWidth) {
      prevWidth = maxHeight;
      prevWidth = maxWidth;
      imageUrls = [];
      nextPage = 1;
      getImages();
    }
  }

  onMount(() => {
    return getImages();
  });
</script>

<style type="text/css">
  .spaced-container {
    padding: 20px;
  }
  input[type="number"] {
    width: 80px; /* setting max width on filter input */
  }
</style>

<section data-component="image-list">
  <nav class="navbar fixed-top navbar-expand bg-dark">
    <div class="container-fluid">
      <div class="text-light h2">Picasso</div>
      <button
        class="btn navbar-btn btn-secondary navbar-right dropdown-toggle"
        type="button"
        id="filterMenu"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false">
        <Icon class="text-light h4" icon={menuIcon} />
      </button>
      <!-- filter dropdown menu -->
      <div
        class="dropdown-menu dropdown-menu-right mx-2"
        aria-labelledby="filterMenu">
        <div class="px-3 mx-3">
          <div class="form-group">
            <label for="width">Max Width</label>
            <input type="number" bind:value={maxWidth} />
            px
          </div>
          <div class="form-group">
            <label for="height">Max Height</label>
            <input type="number" bind:value={maxHeight} />
            px
          </div>
          <button on:click={applyFilter} class="btn btn-primary">Apply</button>
        </div>
      </div>
    </div>
  </nav>
  <div class="spaced-container p-5" />
  <!-- loading screen -->
  {#if isLoading}
    <div
      class="d-flex justify-content-center align-items-center bg-spinner my-4">
      <div class="spinner-border" role="status" />
    </div>
  <!-- no results -->
  {:else if !imageUrls || !imageUrls.length}
    <h3 class="text-center mt-5">
      No images found!
      <Icon icon={notFoundIcon} />
      <br />
      Try changing your filter parameters.
    </h3>
  {:else}
    <!-- show images -->
    {#each imageUrls as imageUrl}
      <ImageListItem imgSrcUrl={imageUrl} />
    {/each}
    <!-- enable pagination if there is a next page -->
    {#if nextPage}
      <div align="center">
        <button
          type="button"
          class="btn btn-secondary my-3"
          on:click|preventDefault={getImages}>
          <span>Load More</span>
        </button>
      </div>
    {/if}
  {/if}
</section>

<script>
  import { writable } from "svelte/store";
  import ImageListItem from "./image-list-item.svelte";

  let nextPage = 1;
  let imageUrls;

  function getImages() {
    fetch(`http://localhost:8000/images/?page=${nextPage}`)
      .then(resp => resp.json())
      .then(function(data) {
        let imageMetadata = data.data;
        let requestPageInfo = data.page_info;

        nextPage = requestPageInfo.next_num;

        let newUrls = imageMetadata.map(
          image =>
            `https://picsum.photos/id/${image.id}/${image.width}/${image.height}`
        );

        imageUrls = imageUrls ? [...imageUrls, ...newUrls] : newUrls;
      });
  }

  getImages();
</script>

<section data-component="image-list">
  {#if imageUrls && imageUrls.length}
    {#each imageUrls as imageUrl}
      <ImageListItem imgSrcUrl={imageUrl} />
    {/each}
  {/if}
  <hr />
  {#if nextPage}
    <div align="center">
      <button on:click={getImages}>Load More</button>
    </div>
  {/if}
</section>

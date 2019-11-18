<script>
  export let imgSrcUrl;

  let toggleGrayscale = false;
  $: sourceUrl = toggleGrayscale ? `${imgSrcUrl}?grayscale` : imgSrcUrl;

  function toggleGrayscaleState() {
    toggleGrayscale = !toggleGrayscale;
  }

  function shareOnFacebook(event) {
    event.preventDefault();
    window.open(
      "https://www.facebook.com/sharer.php?u=" + sourceUrl,
      "popup",
      "width=480,height=320"
    );
  }

  function shareOnTwitter(event) {
    event.preventDefault();
    window.open(
      `https://twitter.com/intent/tweet?url=${sourceUrl}`,
      "popup",
      "width=480,height=320"
    );
  }
</script>

<style>
  svg {
    margin-right: 8px;
    fill: currentColor;
    width: 24px;
    height: 24px;
  }
</style>

<section data-component="image-list-item">
  <div align="center" class="container-fluid p-3">
    <div class="row row-offset-md-4">
      <div class="container-fluid">
        <img
          class="shadow-sm img-fluid img-thumbnail rounded float-center"
          src={sourceUrl}
          alt="Pastebin" />
      </div>
    </div>

    <div class="row p-3">
      <div align="center" class="container">
        <button
          class="btn btn-primary"
          data-toggle="button"
          aria-pressed="false"
          autocomplete="off"
          on:click={toggleGrayscaleState}>
          Toggle Grayscale
        </button>
      </div>
    </div>

    <div class="share-btn">
      <button class="badge badge-primary" on:click={shareOnFacebook}>
        <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 64.8 124.2">
          <path
            d="M42.9,68.4c0-.3,0-.3.3-.3H61.5a.29.29,0,0,0,.3-.3c.3-2.7,2.7-21.9,2.7-22.2H43.2c-.3,0-.3,0-.3-.3v-15c0-1.2.3-3,.3-3.9.3-2.7,2.7-4.2,5.1-5.1a29.11,29.11,0,0,1,5.1-.3H64.8V.9C63.9.9,49.5,0,46.5,0A31.82,31.82,0,0,0,32.7,3c-5.7,3-9.3,7.2-12,13.2-.9,2.7-1.2,4.8-1.8,7.2a44.31,44.31,0,0,0-.3,6.3v15c0,.3,0,.3-.3.3H0V67.2H18.3c.3,0,.3,0,.3.3v56.7h24C42.9,124.2,42.9,85.8,42.9,68.4Z" />
        </svg>
        Share
      </button>
      <button class="badge badge-primary" on:click={shareOnTwitter}>
        <svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 111.9 90.3">
          <title>Twitter</title>
          <path
            d="M111.9,10.8a40.67,40.67,0,0,1-13.2,3.3,23.43,23.43,0,0,0,9.9-12.3A39.61,39.61,0,0,1,93.9,7.5,22.73,22.73,0,0,0,54.3,22.8a29.11,29.11,0,0,0,.3,5.1A64.26,64.26,0,0,1,7.5,3.9a21.26,21.26,0,0,0-3,11.7A22.17,22.17,0,0,0,14.7,34.5a19.38,19.38,0,0,1-10.2-3v.3A22.55,22.55,0,0,0,22.8,54a36,36,0,0,1-6,.9,19.81,19.81,0,0,1-4.2-.3c3,9,11.1,15.3,21.3,15.9A46.64,46.64,0,0,1,5.7,80.4,36.31,36.31,0,0,1,0,80.1,65.67,65.67,0,0,0,34.8,90.3C77.1,90,99.9,55.2,99.9,25.2v-3A43.46,43.46,0,0,0,111.9,10.8Z" />
        </svg>
        Tweet
      </button>
    </div>

  </div>
</section>

<script context="module">
  import Icon from "fa-svelte";
  import { faAdjust } from "@fortawesome/free-solid-svg-icons";
  import { faFacebookF, faTwitter } from "@fortawesome/free-brands-svg-icons";

  let grayscaleToggle = faAdjust;
  let fbIcon = faFacebookF;
  let twitterIcon = faTwitter;
</script>

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
      "width=480,height=320" // set fixed window size
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
    fill: currentColor;
    width: 24px;
    height: 24px;
  }
</style>

<section data-component="image-list-item">
  <div class="container-fluid mx-auto p-3">
    <!-- image container -->
    <div class="row">
      <div class="container-fluid">
        <img
          class="shadow-sm d-block mx-auto img-fluid img-thumbnail rounded"
          src={sourceUrl}
          alt="Pastebin" />
      </div>
    </div>
    
    <!-- image controls container -->
    <div class="row py-2">
      <div class="d-block mx-auto float-center">
        <button
          class="btn btn-primary"
          data-toggle="tooltip"
          on:click={toggleGrayscaleState}
          data-placement="bottom" 
          title="Toggle Grayscale">
          <Icon style="text-light h-4" icon={grayscaleToggle} />
        </button>
        <button 
          class="btn btn-primary" 
          data-toggle="tooltip"
          data-placement="bottom" 
          title="Share on Facebook"
          on:click={shareOnFacebook}>
          <Icon style="text-light h-4" icon={fbIcon} />
        </button>
        <button 
          class="btn btn-primary" 
          data-toggle="tooltip"
          data-placement="bottom" 
          title="Share on Twitter"
          on:click={shareOnTwitter}>
          <Icon style="text-light h-4" icon={twitterIcon} />
        </button>
      </div>
    </div>

  </div>
</section>

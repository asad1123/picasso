<script>
  export let imgSrcUrl;

  let toggleGrayscale = false;
  $: sourceUrl = toggleGrayscale ? `${imgSrcUrl}?grayscale` : imgSrcUrl;

  function toggleGrayscaleState() {
    toggleGrayscale = !toggleGrayscale;
  }
</script>

<section data-component="image-list-item">
  <table align="center">
    <tr>
      <td>
        <img id="image" src={sourceUrl} alt="Pastebin" />
      </td>
    </tr>
    <tr>
      <td align="center">
        <button on:click={toggleGrayscaleState}>Toggle Grayscale</button>
      </td>
    </tr>
  </table>
</section>

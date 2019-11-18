<script>
  import ImageList from "./image-module/image-list.svelte";
</script>

<style>
  .encapsulate {
    max-width: 800px;
    margin: auto;
  }
</style>

<svelte:head>
  <style>
    body {
      background-color: darkgray;
    }
  </style>
</svelte:head>

<div class="encapsulate">
  <ImageList />
</div>

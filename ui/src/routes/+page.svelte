<script lang="ts">
  import Dropzone from "svelte-file-dropzone";
  import { ACCEPTED_FILE_TYPES } from "$lib/constants";

  let file: File = null;

  function handleFilesSelect(e: CustomEvent) {
    const { acceptedFiles, fileRejections } = e.detail;
    file = acceptedFiles?.[0] ?? null;
  }
</script>

<h1 class="text-4xl font-black">Unreceiptify</h1>

<div>
  <Dropzone
    accept={ACCEPTED_FILE_TYPES}
    on:drop={handleFilesSelect}
    disableDefaultStyles
    containerClasses="
    flex items-center justify-center p-20 border border-dashed border-white border-2
    rounded-xl hover:bg-slate-900 transition transition-[background-color] duration-200
    "
  >
    {#if file}
      {file.name}
    {:else}
      Click or drag 'n' drop a file to upload
    {/if}
  </Dropzone>
</div>

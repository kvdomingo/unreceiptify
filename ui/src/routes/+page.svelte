<script lang="ts">
  import Dropzone from "svelte-file-dropzone";
  import { ACCEPTED_FILE_TYPES } from "$lib/constants";
  import { DotLottieSvelte } from "@lottiefiles/dotlottie-svelte";
  import { createMutation } from "@tanstack/svelte-query";
  import { api } from "$lib/api";

  const mutation = createMutation({
    mutationFn: api.testUpload,
    mutationKey: ["upload"],
  });

  function handleFilesSelect(e: CustomEvent) {
    const { acceptedFiles } = e.detail;

    if (acceptedFiles.length() == 0) return;

    const file: File = acceptedFiles[0];
    const blob = new Blob([file], { type: file.type });

    const formData = new FormData();
    formData.append("file", blob);

    $mutation.mutate(formData);
  }
</script>

<h1 class="text-4xl font-black">Unreceiptify</h1>

<div>
  {#if $mutation.isPending}
    <div class="w-96">
      <DotLottieSvelte
        src="https://lottie.host/71960ec6-a158-4896-ac1c-5566c6ee19ed/YtzLabyIS5.lottie"
        autoplay
        loop
      />
    </div>
  {:else if $mutation.data}
    {@const data = $mutation.data?.data ?? {}}
    {#each Object.entries(data) as [key, value]}
      <ul>
        <li>
          <b>{key}</b>: {value}
        </li>
      </ul>
    {/each}
  {:else}
    <Dropzone
      accept={ACCEPTED_FILE_TYPES}
      multiple={false}
      on:drop={handleFilesSelect}
      disableDefaultStyles
      containerClasses="
      flex items-center justify-center p-20 border border-dashed border-white border-2
      rounded-xl hover:bg-slate-900 transition transition-[background-color] duration-200
      "
    />
  {/if}
</div>

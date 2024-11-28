<script lang="ts">
  import Dropzone from "svelte-file-dropzone";
  import { ACCEPTED_FILE_TYPES } from "$lib/constants";
  import { DotLottieSvelte } from "@lottiefiles/dotlottie-svelte";
  import { createMutation } from "@tanstack/svelte-query";
  import { api } from "$lib/api";
  import { heicTo, isHeic } from "heic-to";
  import { Table } from "@/components/ui/table";
  import {
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
  } from "@/components/ui/table/index.js";
  import { Button } from "@/components/ui/button";
  import { MOCK_DATA, MOCK_RESPONSE } from "@/mock";

  let imgSrc: string | null = null;
  let file: File | null = null;
  let previewFile: File | null = null;

  const mutation = createMutation({
    mutationKey: ["upload"],
    mutationFn: async (fileObj: File) => {
      if (await isHeic(fileObj)) {
        previewFile = new File(
          [
            await heicTo({
              blob: fileObj,
              type: "image/jpeg",
              quality: 0.9,
            }),
          ],
          fileObj.name,
          { type: "image/jpeg" },
        );
      } else {
        previewFile = fileObj;
      }

      const blob = new Blob([previewFile], { type: fileObj.type });

      const reader = new FileReader();
      reader.onloadend = async () => {
        console.log(reader.result);
        imgSrc = reader.result as string;
      };
      reader.readAsDataURL(blob);

      // const body = new FormData();
      // body.append("file", fileObj);
      // return await api.upload(body);
    },
  });

  async function handleFilesSelect(e: CustomEvent) {
    const { acceptedFiles } = e.detail;

    if ([...acceptedFiles].length == 0) return;

    file = acceptedFiles[0];
    $mutation.mutate(file!);
  }

  function handleReset() {
    imgSrc = null;
    file = null;
    previewFile = null;
    $mutation.reset();
  }
</script>

<h1 class="text-4xl font-black">Unreceiptify</h1>

<div class="container flex justify-center">
  {#if $mutation.isPending}
    <div class="w-96">
      <DotLottieSvelte
        src="https://lottie.host/71960ec6-a158-4896-ac1c-5566c6ee19ed/YtzLabyIS5.lottie"
        autoplay
        loop
      />
    </div>
    <!--{:else if $mutation.data}-->
    <!--  {@const data = $mutation.data?.data ?? {}}-->
    <!--  {#each Object.entries(data) as [key, value]}-->
    <!--    <ul>-->
    <!--      <li>-->
    <!--        <b>{key}</b>: {value}-->
    <!--      </li>-->
    <!--    </ul>-->
    <!--  {/each}-->
  {:else if imgSrc && file}
    <!--{@const data = $mutation.data?.data ?? {}}-->
    <div class="grid grid-cols-2 gap-12">
      <div>
        <img src={imgSrc} alt={file.name} />
      </div>
      <div>
        <Table>
          <TableCaption>Receipt details</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead class="font-bold">Field</TableHead>
              <TableHead>Value</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {#each Object.entries(MOCK_DATA) as [key, value]}
              <TableRow>
                <TableCell>{key}</TableCell>
                <TableCell>
                  {value ?? "N/A"}
                </TableCell>
              </TableRow>
            {/each}
          </TableBody>
        </Table>

        <Table>
          <TableCaption>Receipt items</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead class="font-bold">Name</TableHead>
              <TableHead>Quantity</TableHead>
              <TableHead>Total Price</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {#each Object.values(MOCK_RESPONSE.items) as value}
              <TableRow>
                <TableCell>{value.description ?? "N/A"}</TableCell>
                <TableCell>{value.quantity ?? "N/A"}</TableCell>
                <TableCell>{value.totalPrice ?? "N/A"}</TableCell>
              </TableRow>
            {/each}
          </TableBody>
        </Table>

        <Button on:click={handleReset}>Start over</Button>
      </div>
    </div>
  {:else}
    <Dropzone
      accept={ACCEPTED_FILE_TYPES}
      multiple={false}
      on:drop={handleFilesSelect}
      disableDefaultStyles
      containerClasses="
      flex items-center justify-center p-20 border border-dashed border-white border-2
      rounded-xl hover:bg-slate-900 transition transition-[background-color,box-shadow] duration-200
      shadow-lg hover:shadow-xl
      "
    />
  {/if}
</div>

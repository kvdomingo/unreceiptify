<script lang="ts">
  import "@fontsource-variable/inter/wght.css";
  import "@fontsource-variable/inter/wght-italic.css";
  import "@fontsource-variable/inter-tight/wght.css";
  import "@fontsource-variable/inter-tight/wght-italic.css";
  import "../app.css";
  import { QueryClientProvider } from "@tanstack/svelte-query";
  import { queryClient } from "$lib/api";
  import { SvelteQueryDevtools } from "@tanstack/svelte-query-devtools";
</script>

<QueryClientProvider client={queryClient}>
  <main class="flex min-h-dvh w-full flex-col items-center justify-center gap-8 py-12">
    <slot />
  </main>

  <SvelteQueryDevtools />
</QueryClientProvider>

<script lang="ts">
  import "@fontsource/geist-sans/100.css";
  import "@fontsource/geist-sans/200.css";
  import "@fontsource/geist-sans/300.css";
  import "@fontsource/geist-sans/400.css";
  import "@fontsource/geist-sans/500.css";
  import "@fontsource/geist-sans/600.css";
  import "@fontsource/geist-sans/700.css";
  import "@fontsource/geist-sans/800.css";
  import "@fontsource/geist-sans/900.css";
  import "../app.css";
  import { QueryClientProvider } from "@tanstack/svelte-query";
  import { queryClient } from "$lib/api";
</script>

<QueryClientProvider client={queryClient}>
  <main class="flex min-h-dvh w-full flex-col items-center justify-center gap-20">
    <slot />
  </main>
</QueryClientProvider>

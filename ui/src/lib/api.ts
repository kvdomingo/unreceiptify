import { browser } from "$app/environment";
import type { Receipt } from "$lib/types";
import { QueryClient } from "@tanstack/svelte-query";
import axios, { type AxiosResponse } from "axios";

const baseURL = "/api";

const axi = axios.create({ baseURL });

export const api = {
  healthCheck(): Promise<AxiosResponse<string>> {
    return axi.get("/health", { responseType: "text" });
  },
  upload(body: FormData): Promise<AxiosResponse<Receipt>> {
    return axi.post("/upload", body);
  },
};

export const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      enabled: browser,
      refetchOnMount: true,
      refetchOnReconnect: true,
      refetchOnWindowFocus: true,
      retry: 3,
    },
    mutations: {
      retry: false,
    },
  },
});

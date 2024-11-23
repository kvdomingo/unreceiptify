import { browser } from "$app/environment";
import { QueryClient } from "@tanstack/svelte-query";
import axios, { type AxiosResponse } from "axios";

const baseURL = "/api";

const axi = axios.create({ baseURL });

export const api = {
  healthCheck(): Promise<AxiosResponse<string>> {
    return axi.get("/api/health", { responseType: "text" });
  },
  upload(body: FormData): Promise<AxiosResponse<string, unknown>> {
    return axi.post("/api/upload", { body });
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

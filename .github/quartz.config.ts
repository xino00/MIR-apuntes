import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "MIR · Apuntes",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "es-ES",
    baseUrl: "mirapuntes.pages.dev",
    ignorePatterns: [".obsidian", "99_Plantillas", "gemini-scribe", "tmp", "README.md", "quartz"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#FAF9F7",
          lightgray: "#EDE9E3",
          gray: "#B5A99A",
          darkgray: "#4A3F35",
          dark: "#1A1208",
          secondary: "#D97757",
          tertiary: "#E8956B",
          highlight: "rgba(217, 119, 87, 0.12)",
          textHighlight: "#FFD6C288",
        },
        darkMode: {
          light: "#1A1410",
          lightgray: "#2E2820",
          gray: "#6B5F55",
          darkgray: "#C8B8A8",
          dark: "#F0E8DF",
          secondary: "#E8876A",
          tertiary: "#D97757",
          highlight: "rgba(217, 119, 87, 0.15)",
          textHighlight: "#CC674488",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({ priority: ["frontmatter", "filesystem"] }),
      Plugin.SyntaxHighlighting({ theme: { light: "github-light", dark: "github-dark" }, keepBackground: false }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({ enableSiteMap: true, enableRSS: true }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config

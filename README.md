# Site Mapper

This is a CLI tool. You give it a top-level domain and it will crawl the sitemap. 

## Features:
* Will detect 404s
* Will generate a sitemap
* Uses a DFS algorithm to focus on top-level pages first
* timeout after 1,000 pages

## Syntax
* Uses `uv`. After downloading, run `uv sync`
* Test with `./test.sh`
* Run with `uv run main <URL> [flags]`

### Flags
* `-v` = Verbose. Useful for debugging, will print everything out.

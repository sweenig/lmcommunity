hostname = hostProps.get("system.hostname")
page = new URL("https://${hostname}/availability").getText()
// println(page + "\n" + "=".multiply(80))
pattern = /<h2 class="lk-simple-title">Looker is (.*)<\/h2>/
if ((page =~ pattern).size() > 0){ //this might be doable with elvis, but this works
  if ((page =~ pattern)[0][1].toLowerCase() == "up") {
    return 0
  } else {
    return 1
  }
}

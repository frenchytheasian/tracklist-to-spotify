<script lang="ts">
  import { TextInput, Button } from "@svelteuidev/core";

  let link = "";
</script>

<div>
  <TextInput
    bind:value={link}
    label="Enter a link to the tracklist on 1001 tracklists"
  />
  <Button />
</div>

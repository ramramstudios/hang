<script>
  export let length = 0;
  export let guessed = [];
  export let revealed = [];
  export let word = [];
</script>

<div class="word">
  {#each Array(length) as _, i}
    <span class="letter">{revealed[i] ? word[i] : '_'}</span>
  {/each}
</div>

<style>
.word {
  font-size: 2rem;
  text-align: center;
  letter-spacing: 0.5rem;
  margin: 1rem 0;
}
.letter {
  display: inline-block;
  width: 1rem;
}
</style>

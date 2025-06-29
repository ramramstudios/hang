<script>
  import { createEventDispatcher } from 'svelte';
  export let guessed = [];
  const dispatch = createEventDispatcher();
  const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

  function guess(letter) {
    dispatch('guess', { letter });
  }
</script>

<div class="keyboard">
  {#each letters as letter}
    <button on:click={() => guess(letter)} disabled={guessed.includes(letter)}>
      {letter}
    </button>
  {/each}
</div>

<style>
.keyboard {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
}
button {
  width: 2rem;
  height: 2rem;
}
</style>

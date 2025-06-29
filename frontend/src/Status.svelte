<script>
  import { createEventDispatcher } from 'svelte';
  export let gameOver = false;
  export let won = false;
  export let word = '';
  const dispatch = createEventDispatcher();
</script>

{#if gameOver}
  <div class="status">
    {#if won}
      <p>You win!</p>
    {:else}
      <p>Game over – the word was {word}</p>
    {/if}
    <button on:click={() => dispatch('again')}>Play Again</button>
  </div>
{/if}

<style>
.status {
  text-align: center;
  margin-top: 1rem;
}
</style>

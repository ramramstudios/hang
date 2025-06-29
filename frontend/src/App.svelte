<script>
  import { onMount } from 'svelte';
  import { game } from './lib/store.js';
  import HangmanDrawing from './HangmanDrawing.svelte';
  import WordDisplay from './WordDisplay.svelte';
  import Keyboard from './Keyboard.svelte';
  import Status from './Status.svelte';

  async function start() {
    const res = await fetch('/api/new-game', { method: 'POST' });
    const data = await res.json();
    game.set({
      gameId: data.gameId,
      length: data.length,
      maxWrong: data.maxWrong,
      guessed: [],
      wrongGuesses: 0,
      revealed: Array.from(data.masked).map(c => c !== '_'),
      word: data.masked.split(''),
      gameOver: false,
      won: false
    });
  }

  onMount(start);

  async function handleGuess(e) {
    const letter = e.detail.letter;
    const res = await fetch('/api/guess', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ gameId: $game.gameId, letter })
    });
    const result = await res.json();
    game.update(g => {
      result.positions.forEach(pos => {
        g.revealed[pos] = true;
        g.word[pos] = letter;
      });
      g.guessed.push(letter);
      g.wrongGuesses = result.wrongGuesses;
      g.gameOver = result.gameOver;
      g.won = result.won;
      if (result.gameOver && result.word) {
        g.word = result.word.split('');
        g.revealed = Array(result.word.length).fill(true);
      }
      return g;
    });
  }

  function playAgain() {
    start();
  }
</script>

<main>
  <h2>Guess the Movie Title!</h2>
  <HangmanDrawing wrongGuesses={$game.wrongGuesses}/>
  <WordDisplay length={$game.length} word={$game.word} revealed={$game.revealed}/>
  <Keyboard guessed={$game.guessed} on:guess={handleGuess}/>
  <Status gameOver={$game.gameOver} won={$game.won} word={$game.word.join('')} on:again={playAgain}/>
</main>

<style>
main {
  max-width: 400px;
  margin: auto;
  text-align: center;
  font-family: sans-serif;
}
</style>

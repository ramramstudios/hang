import { writable } from 'svelte/store';

export const game = writable({
  gameId: null,
  length: 0,
  maxWrong: 6,
  guessed: [],
  wrongGuesses: 0,
  revealed: [],
  gameOver: false,
  won: false
});

<script>
  export let wrongGuesses = 0;
</script>

<svg width="200" height="250" class="hangman">
  <!-- scaffold -->
  <line x1="20" y1="230" x2="180" y2="230" stroke="black"/>
  <line x1="60" y1="230" x2="60" y2="20" stroke="black"/>
  <line x1="60" y1="20" x2="140" y2="20" stroke="black"/>
  <line x1="140" y1="20" x2="140" y2="40" stroke="black"/>

  {#if wrongGuesses > 0}
    <!-- head -->
    <circle cx="140" cy="55" r="15" stroke="black" fill="none"/>
  {/if}
  {#if wrongGuesses > 1}
    <!-- torso -->
    <line x1="140" y1="70" x2="140" y2="120" stroke="black"/>
  {/if}
  {#if wrongGuesses > 2}
    <!-- left arm -->
    <line x1="140" y1="80" x2="120" y2="100" stroke="black"/>
  {/if}
  {#if wrongGuesses > 3}
    <!-- right arm -->
    <line x1="140" y1="80" x2="160" y2="100" stroke="black"/>
  {/if}
  {#if wrongGuesses > 4}
    <!-- left leg -->
    <line x1="140" y1="120" x2="125" y2="150" stroke="black"/>
  {/if}
  {#if wrongGuesses > 5}
    <!-- right leg -->
    <line x1="140" y1="120" x2="155" y2="150" stroke="black"/>
  {/if}
</svg>

<style>
.hangman {
  display: block;
  margin: auto;
}
</style>

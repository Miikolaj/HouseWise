<script lang="ts">
	export let value = false;
	export let title: string = 'Place Holder';

	function toggle() {
		value = !value;
	}
</script>

<div class="wrapper">
	<button class="radio-button" type="button" on:click={toggle} aria-pressed={value}>
		{#if value}
			<div class="dot"></div>
		{/if}
	</button>
	<div class="title">
		{title}
	</div>
</div>

<style lang="scss">
  .radio-button {
    display: inline-block;
    width: 24px;
    height: 24px;
    border: 2px solid $primary;
    border-radius: 50%;
    position: relative;
    cursor: pointer;
  }

  .radio-button .dot {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 12px;
    height: 12px;
    background-color: $primary;
    border-radius: 50%;
  }

	.wrapper{
		display: flex;
    align-items: center;
		gap: 10px;
	}
</style>
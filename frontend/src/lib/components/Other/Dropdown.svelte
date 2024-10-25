<script lang="ts">
	import Fa from 'svelte-fa';
	import { faCaretDown } from '@fortawesome/free-solid-svg-icons';

	export let name: string = '-- None --';
	export let title: string = 'Placeholder';
	export let width: number = 120;
	export let options: string[] = ['Excellent', 'Good', 'Fair', 'Poor'];
	export let selectedOption: string = options[3];
</script>

<div class="wrapper">
	<div class="title">
		{title}
	</div>
	<div class="select-container" style="width: {width}px">
		<select
			name={name}
			bind:value={selectedOption}
		>
			{#each options as option}
				<option value={option}>{option}</option>
			{/each}
		</select>
		<div class="icon">
			<Fa icon={faCaretDown} size="1x" />
		</div>
	</div>
</div>

<style lang="scss">
  .wrapper {
    display: grid;
    gap: 5px;
  }

  .select-container {
    position: relative;
    display: inline-block;
    width: 100%;
  }

  select {
    width: 100%;
    background: $secondary;
    border: 1px solid $primary;
    color: $font-color;
    border-radius: 4px;
    padding: 12px;
  }

  .icon {
    position: absolute;
    top: 50%;
    right: 12px;
    transform: translateY(-50%);
    pointer-events: none;
    color: lighten($accent,10%);
  }

</style>

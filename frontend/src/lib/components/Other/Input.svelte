<script lang="ts">

	export let name: string = '-- None --';
	export let placeholder: string = 'ex. 23';
	export let title: string = 'Placeholder';
	export let width: number = 12;
</script>

<div class="wrapper">
	<div class="title">
		{title}
	</div>
	<input style="width: {width}px"
				 name={name}
				 type="text"
				 placeholder={placeholder}
	/>
</div>

<style lang="scss">
	.wrapper{
		display: grid;
		gap: 5px;
	}
  input {
    background: $secondary;
    border: 1px solid $primary;
    color: $font-color;
    border-radius: 4px;
    padding: 12px;
  }
</style>
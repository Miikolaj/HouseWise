<script lang="ts">
	export let href = '#';
	export let type = 'default';
</script>


<a class='default {type}' href={href}>
		<slot />
</a>

<style lang="scss">
	.default{
		display: inline-flex;
    justify-content: center;
		align-items: center;
	}

	.estimate{
		padding: 18px 48px;
		border-radius: 40px;
		background: $primary;
    box-shadow: 0 0 25px 10px rgba(66, 32, 133, 0.50);
    transition: background 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
		font-size: 1.125rem;
		font-weight: 600;
    &:hover {
      background: lighten($primary, 10%);
      transform: translatey(-5px);
      box-shadow: 0 15px 30px rgba(66, 32, 133, 0.6);
    }

    &:focus {
      outline: none;
    }
	}

	.form{
		width: 100%;
    padding: 15px 0;
		background: $primary;
		border-radius: 4px;
    box-shadow: 0 0 25px 10px rgba(58, 49, 216, 0.50);
    transition: background 0.3s ease,  box-shadow 0.3s ease;
		justify-self: center;
    &:hover {
      background: lighten($primary, 10%);
      box-shadow: 0 0 25px 10px rgba(66, 32, 133, 0.6);
    }

    &:focus {
      outline: none;
    }
	}
</style>
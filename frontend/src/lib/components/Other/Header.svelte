<script lang="ts">
	import { onMount } from 'svelte';
	import Fa from 'svelte-fa';
	import {faCity} from '@fortawesome/free-solid-svg-icons';
	import Button from '$components/Buttons/Button.svelte';

	let scrolled = false;

	const handleScroll = () => {
		scrolled = window.scrollY > 200;
	};

	onMount(() => {
		window.addEventListener('scroll', handleScroll);
		return () => {
			window.removeEventListener('scroll', handleScroll);
		};
	});
</script>

<div class="header {scrolled ? 'scrolled' : 'default'}">
	<div class="header-content">

		<div class="name">HouseWise</div>
		<div class="links">
			<Button href="#main">Main</Button>
			<Button href="#program">Program</Button>
			<Button href="#about">About</Button>
		</div>
		<div class="logo">
			<Fa icon={faCity} />
		</div>

	</div>
</div>

<style lang="scss">
  .header {
    position: fixed;
    width: 100%;
    transition: background-color 0.3s ease-in-out;
    z-index: 9999;
    background-color: transparent;

    &.scrolled {
      background-color: $background;
			border-bottom: solid 1px $accent;
    }
  }

  .header-content {
    display: flex;
    align-items: center;
    padding: 15px 80px;
  }

  .name {
    flex: 1;
    font-size: 1.5rem;
    font-weight: 700;
  }

  .links {
    display: inline-flex;
    align-items: center;
    gap: 40px;
  }

  .logo {
    flex: 1;
    display: flex;
    justify-content: flex-end;
  }


</style>

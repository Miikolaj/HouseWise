<script lang="ts">
	import Button from '$components/Buttons/Button.svelte';
</script>


<div id="main" class="main-section">
	<div class="content">
		<div class="text-wrapper">
			<div class="title">Get price you deserve</div>
			<div class="slogan">Advanced ai tool to estimate cost of housing space</div>
		</div>
		<Button type="estimate" href="#program">Estimate</Button>
	</div>
</div>

<style lang="scss">
  .main-section {
    height: 100vh;
    background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('$assets/gothamCity.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 20px;
  }

  .title {
    font-size: 4.5rem;
    text-transform: uppercase;
    font-weight: 700;
  }

  .slogan {
    font-size: 1.125rem;
    font-weight: 200;
  }
</style>

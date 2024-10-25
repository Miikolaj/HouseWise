<script lang="ts">
	import { Input, Button, Radio, Dropdown } from '$components';
	let radioValue = false;
</script>

<div id="program" class="program-section">
	<div class="container">
		<div>
			<div class="bold">
				Your estimate: 0zł
			</div>
			<div class="regular">
				Enter Your Property Details to Estimate Its Value
			</div>
		</div>
		<div class="form">
			<div class="single-line">
				<Input width={170} title="Area"/>
				<Input width={110} title="Bedrooms"/>
			</div>
			<div class="single-line">
				<Input width={100} title="Bathrooms"/>
				<Input width={180} title="Floors"/>
			</div>
			<div class="single-line">
				<Input width={140} title="Year Built"/>
				<Dropdown width={140} title="Condition"/>
			</div>
			<div class="single-line">
				<Input width={300} title="Location"/>
			</div>
			<div class="single-line">
				<Radio bind:value={radioValue} title="Has garage?"/>
			</div>
			<div class="single-line">
				<Button type="form" >Submit</Button>
			</div>
		</div>
	</div>
</div>

<style lang="scss">
  .program-section {
    height: 100vh;
    padding: 5% 10%;
  }

  .container {
    width: 100%;
    height: 100%;
  }

  .bold {
    font-size: 4.5rem;
    font-weight: 700;
  }

  .form {
    padding-top: 30px;
    display: grid;
    gap: 20px;
    max-width: 300px;
  }

  .single-line {
    display: flex;
    gap: 20px;
  }
</style>

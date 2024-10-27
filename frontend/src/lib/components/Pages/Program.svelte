<script lang="ts">
    import {Input, Button, Radio, Dropdown} from '$components';
    import {PriceRepository} from "$lib/repositories/price.repository";

    let radioValue = false;
    let condition = '';
    let location = '';
    let area = '';
    let bedrooms = '';
    let bathrooms = '';
    let floors = '';
    let yearOfBuilt = '';
    let price: string = '0';


    const priceRepository = new PriceRepository();

    const validate = (value: string) => {
        let regex: RegExp = /^\d+$/;
        if (!value.trim()) {
            return 'Field cannot be empty';
        } else if (!regex.test(value.trim())) {
            return 'Please enter a valid number';
        }
        return '';
    };

    const validateYear = (value: string) => {
        let regex: RegExp = /^(17\d{2}|18\d{2}|19\d{2}|20[0-4]\d|2050)$/;
        if (!value.trim()) {
            return 'Field cannot be empty';
        } else if (!regex.test(value.trim())) {
            return 'Please enter a valid year';
        }
        return '';
    };

    const submitForm = async () => {
        if (validate(area) || validate(bedrooms) || validate(bathrooms) || validate(floors) || validateYear(yearOfBuilt)) {
            return;
        }

        try {
            price = await priceRepository.getPrice(area, bedrooms, bathrooms, floors, condition, location, yearOfBuilt, radioValue);
        } catch (error) {
            console.error('Error fetching price:', error);
        }
    }
</script>

<div id="program" class="program-component">
    <div class="form-container">
        <div>
            <div class="form-header">
                Your estimate: {price}zł
            </div>
            <div class="form-description">
                Enter Your Property Details to Estimate Its Value
            </div>
        </div>
        <div class="form-wrapper">
            <Input title="Area in square meters" placeholder="e.g., 120" bind:value={area} {validate}/>
            <Input title="Bedrooms count" placeholder="e.g., 3" bind:value={bedrooms} {validate}/>
            <Input title="Bathrooms count" placeholder="e.g., 2" bind:value={bathrooms} {validate}/>
            <Input title="Amount of Floors" placeholder="e.g., 1" bind:value={floors} {validate}/>
            <Dropdown title="Condition" options={['Excellent', 'Good', 'Fair', 'Poor']}
                      bind:selectedOption={condition}/>
            <Dropdown title="Location" options={['Downtown', 'Urban', 'Suburban', 'Rural']}
                      bind:selectedOption={location}/>
            <Input title="Year of Built" placeholder="e.g., 1995" bind:value={yearOfBuilt} validate={validateYear}/>
            <div class="radio-wrapper">
                <div>&zwnj;</div>
                <Radio bind:value={radioValue} title="Has garage?"/>
            </div>
        </div>
        <Button type="form" on:click={submitForm}>Submit</Button>
    </div>
</div>

<style lang="scss">
  .program-component {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;

    .form-header {
      font-size: 4.5rem;
      font-weight: 700;
    }

    .form-description {
      font-size: 1.2rem;
    }
  }

  .form-container {
    display: grid;
    text-align: center;
    gap: 40px;
    place-items: center;
  }

  .form-wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0 20px;
    max-width: 500px;
  }

  .radio-wrapper {
    gap: 5px;
  }
</style>

<script lang="ts">
    import {Button, Dropdown, Input} from '$components';
    import {PriceRepository} from "$lib/repositories/price.repository";

    let price: string = '0';
    let OverallQual: string = '';
    let GarageCars: string = '';
    let ExterQual: string = '';
    let GrLivArea: string = '';
    let FullBath: string = '';
    let KitchenQual: string = '';
    let YearBuilt: string = '';
    let FirstFlrSF: string = '';
    let BsmtQual: string = '';
    let Fireplaces: string = '';

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
        if (validate(GarageCars) || validate(GrLivArea) || validate(FullBath) || validate(FirstFlrSF) || validateYear(YearBuilt) || validate(Fireplaces)) {
            return;
        }

        try {
            price = await priceRepository.getPrice(
                OverallQual,
                GarageCars,
                ExterQual,
                GrLivArea,
                FullBath,
                KitchenQual,
                YearBuilt,
                FirstFlrSF,
                BsmtQual,
                Fireplaces
            );
            console.log('Predicted Price:', price);
        } catch (error) {
            console.error('Error fetching price:', error);
        }
    }
</script>

/**
* TODO: Add better validation and display error messages
*/

<div id="program" class="program-component">
    <div class="form-container">
        <div>
            <div class="form-header">
                Your estimate: {price} zł
            </div>
            <div class="form-description">
                Enter Your Property Details to Estimate Its Value
            </div>
        </div>
        <div class="form-wrapper">
            <Dropdown title="Overall Quality"
                      options={['Very Excellent', 'Excellent', 'Very Good', 'Good', 'Above Average', 'Average', 'Below Average', 'Fair', 'Poor', 'Very Poor']}
                      bind:selectedOption={OverallQual}/>
            <Input title="Car capacity in garage" placeholder="e.g. 2" bind:value={GarageCars}
                   validate={validate}/>
            <Dropdown title="External Quality" options={['Excellent', 'Good', 'Average/Typical', 'Fair', 'Poor']}
                      bind:selectedOption={ExterQual}/>
            <Input title="Above ground sq. ft." placeholder="e.g. 2400" bind:value={GrLivArea}
                   validate={validate}/>
            <Input title="Number of bathrooms" placeholder="e.g. 1" bind:value={FullBath}
                   validate={validate}/>
            <Dropdown title="Kitchen quality" options={['Excellent', 'Good', 'Average/Typical', 'Fair', 'Poor']}
                      bind:selectedOption={KitchenQual}/>
            <Input title="Year the House Was Built" placeholder="e.g. 2002" bind:value={YearBuilt}
                   validate={validateYear}/>
            <Input title="First Floor square feet" placeholder="e.g. 4000" bind:value={FirstFlrSF}
                   validate={validate}/>
            <Dropdown title="Basement quality" options={['Excellent', 'Good', 'Typical', 'Fair', 'Poor','No Basement']}
                      bind:selectedOption={BsmtQual}/>
            <Input title="Number of fireplaces" placeholder="e.g. 1" bind:value={Fireplaces}
                   validate={validate}/>
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

  @media (max-width: 580px) {
    .program-component .form-header {
      font-size: 2rem !important;
    }

    .program-component .form-description {
      font-size: 1rem !important;
    }


  }
</style>

<script lang="ts">

</script>

<div id="about" class="about-section">
    <div class="left-section">
        <div class="header">How it works?</div>
        <div class="text">The HouseWise estimator predicts house prices using a <span>machine learning model</span>
            trained on
            property data such as area, number of bedrooms, bathrooms, floors, year built, location, condition, garage,
            and
            price.
        </div>
        <div class="text">The model utilizes the<span>RandomForestRegressor</span>, machine learning algorithm
            based on an ensemble of decision trees. The model works by constructing multiple decision trees during
            training and combining their outputs to refine price predictions. Additionally it reduces the risk of overfitting
            compared to a single decision tree.
        </div>
        <div class="text">When users input details about a house, the estimator analyzes the data and predicts the
            price based on learned relationships between features. The result is a <span>reliable estimate</span> of the
            house’s value,
            helping users make informed decisions in the real estate market.
        </div>
    </div>

    <div class="right-section">
        <div class="dropdown-component">
            <div class="stat">250.000+</div>
            <div class="text">Trusted Homebuyers and Sellers</div>
        </div>
        <div class="dropdown-component">
            <div class="stat">15,000+</div>
            <div class="text">Hours Saved in Market Research</div>
        </div>
        <div class="dropdown-component">
            <div class="stat">90%</div>
            <div class="text">Satisfied Users</div>
        </div>
    </div>
</div>

<style lang="scss">
  .about-section {
    height: 100vh;
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: center;
    justify-items: center;
    padding: 0 5rem;
  }

  .left-section {
    display: flex;
    flex-direction: column;
    gap: 1.875rem;
    max-width: 50rem;
  }

  .header {
    font-size: 4.5rem;
    font-weight: 700;
  }

  .text {
    font-size: 1.375rem;
  }

  span {
    color: $primary;
    font-weight: 600;
  }

  .right-section {
    display: flex;
    flex-direction: column;
    gap: 1.875rem;
    background: white;
    max-width: 37.5rem;
    padding: 1.875rem;
    border-radius: 1.875rem;
    background: linear-gradient(180deg, #010104 5%, #3A31D8 100%);
  }

  .stat {
    font-size: 2rem;
    font-weight: 600;
  }

  @media (max-width: 1180px) {
    .about-section {
      grid-template-columns: 1fr;
      padding: 20px 20px;
      gap: 20px;
    }
  }

  @media (max-width: 992px) {
    .header {
      font-size: 2rem;
    }
  }
</style>

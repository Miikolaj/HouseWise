<script lang="ts">
    import Fa from 'svelte-fa';
    import {faCaretDown} from '@fortawesome/free-solid-svg-icons';

    export let name: string = '-- None --';
    export let title: string = '-- None --';
    export let options: string[] = ['Excellent', 'Good', 'Fair', 'Poor'];
    export let selectedOption: string = '';
    export let placeholder: string = '-- None --';

    let selectClass = 'placeholder';

    const handleChange = (event: Event) => {
        const selectElement = event.target as HTMLSelectElement;
        selectClass = selectElement.value ? 'selected' : 'placeholder';
    };

    export let validate: (value: string) => string;
    let error = '';

    const handleBlur = () => {
        error = validate(selectedOption);
    };
</script>

<div class="dropdown-component">
    <div class="title">
        {title}
    </div>
    <div class="select-wrapper">
        <select
                class="select-option {selectClass}"
                name={name}
                bind:value={selectedOption}
                on:change={handleChange}
                on:blur={handleBlur}
        >
            <option value="" disabled selected hidden>
                {placeholder}
            </option>

            {#each options as option}
                <option value={option}>{option}</option>
            {/each}
        </select>
        <div class="icon-container">
            <Fa icon={faCaretDown} size="1x"/>
        </div>
    </div>
    <div class="error-wrapper">
        {error || "\u00A0"}
    </div>
</div>

<style lang="scss">
  .dropdown-component {
    display: grid;
    width: 100%;
    text-align: left;
  }

  .title {
    font-weight: 500;
    padding-bottom: 5px;
  }

  .select-wrapper {
    position: relative;
    display: inline-block;
  }

  .select-option {
    width: 100%;
    background: $secondary;
    border: 1px solid $primary;
    color: $font-color;
    border-radius: 4px;
    padding: 12px;

    &.placeholder {
      color: #ebe9fc80;
    }

    &.selected {
      color: $font-color;
    }
  }

  .icon-container {
    position: absolute;
    top: 50%;
    right: 12px;
    transform: translateY(-50%);
    pointer-events: none;
    color: lighten($accent, 10%);
  }

  .error-wrapper {
    color: #FF4C4C;
    font-size: 0.8rem;
    padding:  7px 0;
  }
</style>
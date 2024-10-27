<script lang="ts">
    import Fa from 'svelte-fa';
    import {faCaretDown} from '@fortawesome/free-solid-svg-icons';

    export let name: string = '-- None --';
    export let title: string = '-- None --';
    export let options: string[] = ['Excellent', 'Good', 'Fair', 'Poor'];
    export let selectedOption: string = '';
    export let placeholder: string = options[0];
</script>

<div class="dropdown-component">
    <div class="title">
        {title}
    </div>
    <div class="select-wrapper">
        <select
                class="select-option"
                name={name}
                bind:value={selectedOption}
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
    {"\u00A0"}
</div>

<style lang="scss">
  .dropdown-component {
    display: grid;
    gap: 5px;
    width: 100%;
    text-align: left;
  }

  .title {
    font-weight: 500;
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
  }

  .icon-container {
    position: absolute;
    top: 50%;
    right: 12px;
    transform: translateY(-50%);
    pointer-events: none;
    color: lighten($accent, 10%);
  }
</style>

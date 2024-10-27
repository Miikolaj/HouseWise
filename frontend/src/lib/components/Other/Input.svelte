<script lang="ts">
    export let name: string = '-- None --';
    export let placeholder: string = '';
    export let title: string = 'Placeholder';
    export let value = '';
    let error = '';

    const handleInput = (event: Event) => {
        const target = event.target as HTMLInputElement;
        value = target.value;
    };
    export let validate: (value: string) => string;
</script>

<div class="input-component">
    <div class="title">
        {title}
    </div>
    <input
            name={name}
            type="text"
            placeholder={placeholder}
            on:input={handleInput}
            on:blur={() => error = validate(value)}
    />
    <div class="error-wrapper">
        {error || "\u00A0"}
    </div>
</div>

<style lang="scss">
  .input-component {
    display: grid;
    width: 100%;
    text-align: left;
  }
  .title{
    padding-bottom: 5px;
    font-weight: 500;
  }

  input {
    background: $secondary;
    border: 1px solid $primary;
    color: $font-color;
    border-radius: 4px;
    padding: 12px;
    &::placeholder {
      color: #ebe9fc80;
    }
  }

  .error-wrapper {
    color: #FF4C4C;
    font-size: 0.8rem;
    padding:  7px 0;
  }
</style>

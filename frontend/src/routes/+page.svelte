<script lang="ts">
    import {About, Main, Program} from '$components';

</script>

<div class="dropdown-component">
    <Main/>
    <Program/>
    <About/>
</div>

<style lang="scss">
    .dropdown-component {
      display: grid;
    }

    @media (max-height: 464px) {
      .dropdown-component {
        gap: 70px;
      }
    }
</style>
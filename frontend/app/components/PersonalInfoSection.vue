<template>
  <div class="personal-info-section" v-if="info.length > 0">
    <h6 class="title is-6 section-title has-text-dark">
      {{ header }}
    </h6>
    <personal-info-item
      v-for="(infoItem, index) in info"
      :value="infoItem[valueProperty]"
      :primary="infoItem.primary"
      :infoType="infoItem.info_type"
      :key="index">
    </personal-info-item>
  </div>
</template>

<script>
  import PersonalInfoItem from './PersonalInfoItem';
  import { CONTACT_HEADER_MAPPING } from "../constants";

  export default {
    name: "personal-info-section",
    components: { PersonalInfoItem, },
    props: {
      type: {
        type: String,
        required: true,
      },
      info: {
        type: Array,
        required: true,
      },
      valueProperty: {
        type: String,
        required: true,
      }
    },

    computed: {
      header() {
        return CONTACT_HEADER_MAPPING[this.type];
      }
    },

  }
</script>

<style lang="scss" scoped>
  .section-title {
    margin-bottom: 0.5rem;
  }

  .personal-info-section {
    margin-bottom: 1rem;

    .title {
      margin-left: 0.15rem;
    }
  }
</style>
<template>
  <b-dropdown position="is-bottom-left" :disabled="disabled">
    <slot slot="trigger"></slot>

    <b-dropdown-item v-if="detail" @click.native.stop="$emit('detailClick')">Detail</b-dropdown-item>
    <b-dropdown-item v-if="edit" @click.native.stop="$emit('editClick')">Edit</b-dropdown-item>
    <b-dropdown-item v-if="remove" @click.native.stop="$emit('removeClick')">Delete</b-dropdown-item>
  </b-dropdown>
</template>

<script>
  export default {
    name: "crud-dropdown",
    props: [
      'detail',
      'edit',
      'remove',
      'disabled'
    ]
  }
</script>

<style scoped>

</style>
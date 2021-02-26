<template>
  <q-page>
    <h4>USER PROFILE PAGE</h4>
    {{ data }}
    <div class="q-gutter-y-md column" style="max-width: 300px">
      <q-input v-model="data.full_name" label="Full Name" :dense="dense" disable readonly />
      <q-input v-model="data.email" label="Email" :dense="dense" disable readonly />
      <q-input v-model="data.related_fund" label="Related Funds" :dense="dense" disable readonly />
      <q-input v-model="data.related_department" label="Related Departments" :dense="dense" disable readonly />
      

    </div>

  </q-page>
</template>

<script>
import { defineComponent, ref, computed } from "vue"; 
import { useStore } from 'vuex'
export default {
  setup() {
    const store = useStore()
    return {
      data: store.getters
    }
  }, // END OF SETUP
};
</script>

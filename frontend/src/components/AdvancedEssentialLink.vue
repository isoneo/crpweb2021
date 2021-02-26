<template>
  <div>
    <div v-if="children.length == 0">
      <q-item
        clickable
        v-ripple
        :icon="icon"
        :inset-level="level"
        @click="send_to_page(link)"
      >
        <div class="row">
          <q-item-section class="col-auto">
            <q-icon :name="icon" />
          </q-item-section>
          <q-item-section class="col-md-auto q-pl-lg">
             <q-item-label> {{ title }} </q-item-label>
             <q-item-label caption> {{ caption }} </q-item-label>
          </q-item-section>
        </div>
      </q-item>
    </div>
    <div v-else>
      <div v-if="children.length > 0">
        <!-- {{children}} -->
        <q-expansion-item
        dense
        dense-toggle
          expand-separator
          :icon="icon"
          :label="title"
          :caption="caption"
          :header-inset-level="level"
          default-closed
          @click="send_to_page(link)"
          
        >
          <AdvancedEssentialLink
            v-for="child in children"
            :key="child"
            v-bind="child"
          >
          </AdvancedEssentialLink>
        </q-expansion-item>
      </div>
      <div v-else>
        <q-item
          clickable
          v-ripple
          :icon="icon"
          :content-inset-level="level"
          @click="send_to_page(link)"
        >
          <q-item-section>
            {{ title }}
          </q-item-section>
        </q-item>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "AdvancedEssentialLink",
  props: {
    title: {
      type: String,
      required: true,
    },

    caption: {
      type: String,
      default: "",
    },

    link: {
      type: String,
      default: "#",
    },

    icon: {
      type: String,
      default: "",
    },

    level: {
      type: String,
      default: "0",
    },

    children: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    send_to_page(link) {
      this.$router.push(link);
    },
  },
};
</script>

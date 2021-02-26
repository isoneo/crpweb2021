<template>
  <q-layout view="lHh lpR fFf">
    <q-header reveal elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title> CRPWeb v0.4 </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
        <q-btn :icon="dark_mode_icon" flat padding="xs" @click="changeDarkMode"/>
        <q-btn
          round
          dense
          flat
          color="white"
          icon="account_box"
          v-if="isLoggedIn"
        >
          <q-menu>
            <q-list style="min-width: 100px">
              <AdvancedEssentialLink
                v-for="link in accLinks"
                :key="link.title"
                v-bind="link"
              />

              <!-- <messages></messages> -->
              <q-card class="text-center no-shadow no-border">
                <q-btn
                  label="View All"
                  style="max-width: 120px !important"
                  flat
                  dense
                  class="text-indigo-8"
                ></q-btn>
              </q-card>
            </q-list>
          </q-menu>
          <!--            <q-tooltip>Notifications</q-tooltip>-->
        </q-btn>
        <q-btn
          flat
          round
          dense
          icon="fas fa-sign-out-alt"
          @click="logoutNotify"
          to="/"
          v-if="isLoggedIn"
        />
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above elevated >
      <q-list>
        <q-item-label header class="text-grey-8">
          Essential Links
        </q-item-label>

        <AdvancedEssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import AdvancedEssentialLink from "components/AdvancedEssentialLink.vue";

const xlinksList = [
  {
    title: "Dashboard",
    caption: "Main Page",
    icon: "fas fa-home",
    link: "/",
  },
  {
    title: "Login",
    caption: "Testing login page",
    icon: "code",
    link: "/login",
  },
  {
    title: "Dashboard",
    caption: "Main Page",
    icon: "home",
    link: "/",
  },
];
const linksList = [
  {
    title: "Dashboard",
    caption: "Main Page",
    icon: "fas fa-home",
    link: "/",
    level: 0,
    children: [],
  },
  {
    title: "Login",
    caption: "Testing login page",
    icon: "code",
    link: "/login",
    level: 0,
    children: [],
  },
  {
    title: "Source & Reference",
    caption: "Sources and reference setup",
    icon: "far fa-folder",
    link: "",
    level: 0,
    children: [
      {
        title: "Fund List",
        caption: "List of Funds in CRPWeb",
        // icon: "home",
        link: "/src_ref/fund",
        level: 0.4,
        children: [],
      },
       {
        title: "Seller List",
        caption: "List of Sellers in CRPWeb",
        // icon: "home",
        link: "/src_ref/seller",
        level: 0.4,
        children: [],
      },
    ],
  },
];
const account_links = [
  {
    title: "View Profile",
    caption: "Edit / View Profile",
    icon: "",
    link: "/user/profile",
    level: 0,
    children: [],
  },
];
import { defineComponent, ref, computed, onMounted } from "vue";
import { useStore } from "vuex";
import { useRouter } from "vue-router";
import { useQuasar } from "quasar";

export default defineComponent({
  name: "MainLayout",

  components: {
    AdvancedEssentialLink,
  },

  setup() {
    const store = useStore();
    const router = useRouter();
    const leftDrawerOpen = ref(false);
    const isLoggedIn = computed(() => store.getters.isLoggedIn);
    const  dark_mode_icon = ref("far fa-lightbulb")
    onMounted(() => store.dispatch("auth/getInfo"));
    const $q = useQuasar();
    return {
      essentialLinks: linksList,
      accLinks: account_links,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
      logoutNotify() {
        store
          .dispatch("auth/logout")
          .then(() => {
            console.log("Successfully logouted");
            router.push("/login");
            // this.$router.push({ name: "login" });
          })
          .catch((error) => {
            console.log("Logut Failed error");
            console.log(error);
          });
      },
      dark_mode_icon,
      changeDarkMode() {
        $q.dark.toggle()
      },
      isLoggedIn,
    };
  }, // END OF SETUP

  // computed: {
  //   isLoggedIn() {
  //     console.log(this.$store.getters.isLoggedIn);
  //     return this.$store.getters.isLoggedIn;
  //   },
  // }, // END OF COMPUTED
  // methods: {
  //   logoutNotify() {
  //     this.$store
  //       .dispatch("auth/logout")
  //       .then(() => {
  //         console.log("Successfully logouted");
  //         // this.$router.push('/login')
  //         this.$router.push({ name: "login" });
  //       })
  //       .catch((error) => {
  //         console.log("Logut Failed error");
  //         console.log(error);
  //       });
  //   },
  // }, // End of Method
});
</script>

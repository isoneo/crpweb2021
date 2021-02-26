<template>
  <q-dialog ref="userEditDialog" @hide="onDialogHide">
    <q-card style="width: 700px; max-width: 85vw;">
      <q-card-section>
        <div class="text-h6">
          {{ modalTitle }}
        </div>
      </q-card-section>
      <div class="q-pa-md">
        <div class="q-gutter-x-lg q-pa-md row">

          <q-input
            filled
            v-model="udata.email"
            label="Email"
            stack-label
            :readonly="localreadonlyFlag"
            
          >
            <template v-slot:prepend>
              <q-icon name="email" />
            </template>
          </q-input>
          <q-input
            filled
            v-model="udata.password"
            label="Password"
            stack-label
            v-if="!localreadonlyFlag"
            
          />
        </div>
        <q-separator inset />
        <div class="q-gutter-x-lg q-pa-md row">
          <div class="q-gutter-y-md q-pa-md column">
            <q-input
              filled
              v-model="udata.first_name"
              label="First Name"
              stack-label
            />
            <q-input
              filled
              v-model="udata.last_name"
              label="Last Name"
              stack-label
            />
            <q-input
              filled
              v-model="udata.company_id"
              label="User Co"
              stack-label
              readonliy
            />
            <q-input
              filled
              v-model="udata.department_id"
              label="User Loc"
              stack-label
            />
          </div>
        </div>
      </div>

      {{ udata }}
      <!--
        ...content
        ... use q-card-section for it?
      -->

      <!-- buttons example -->
      <q-card-actions align="right">
        <q-btn color="primary" label="OK" @click="onOKClick" />
        <q-btn color="primary" label="Cancel" @click="onCancelClick" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import { userDetailInfo, userPatchInfo, userRegister } from "src/api/auth";
export default {
  name: "ModalUserInfoEdit",
  props: {
    user_id: {
      type: [Number, String],
      required: true,
    },
    op_type: {
      type: [String],
      required: true,
    },
    // ...your custom props
  },
  data() {
    return {
      udata: [],
      localreadonlyFlag: true,
    };
  }, // END OF DATA
  watch: {
    user_id: function(val, oldval) {
      console.log(val);
      console.log(oldval);
      if (val !== "" && this.op_type === "Update") {
        this.getUserData(val);
      }
    },
    op_type: function(val, oldval) {
      if (val === "Create") {
        this.localreadonlyFlag = false;
      } else {
        this.localreadonlyFlag = true;
      }
    },
  },
  computed: {
    modalTitle: function() {
      if (this.op_type === "Update") {
        return (
          "User Data Edit for " +
          this.udata.first_name +
          " " +
          this.udata.last_name
        );
      } else {
        return "Create New User";
      }
    },
  },
  methods: {
    getUserData(user_id) {
      userDetailInfo(user_id).then((response) => {
        this.udata = response.data;
      });
    },
    resetUserData() {
      this.udata = [];
    },
    setupBlankForm() {
      this.udata = {        
        first_name: "",
        last_name: "",
        password: "",
        // password_confirm: "",
        email: "",

        company_id: 1,
        department_id: 1,        
        role_id: 110,
      };
    },
    createNewUser() {
      console.log(this.udata)

      userRegister(this.udata).then((response) => {
        console.log(response);
      }).catch(error => {
        this.$q.notify({
          message: "New User creation failed. Check email format",
          color:'red'
        })
        console.log(error)
      })
    },
    changeUsername($event){
      if(this.op_type ==="Create"){
        this.udata.username = $event
      }
    },
    confirmPWD($event) {
      if(this.op_type==="Create"){
        this.udata.password_confirm = $event
      }
    },
    patchUserData() {
      // var final_user_data = {
      //   address: "",
      //   first_name: this.first_name,
      //   last_name: this.last_name,
      //   mobile: "",
      //   phone: "",
      // };

      userPatchInfo(this.user_id, this.udata)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // following method is REQUIRED
    // (don't change its name --> "show")
    show() {
      // console.log(this.user_id);
      // console.log(this.op_type === "Create");
      // console.log(this.localreadonlyFlag);
      if (this.op_type === "Create") {
        this.setupBlankForm();
      }
      this.$refs.userEditDialog.show();
    },

    // following method is REQUIRED
    // (don't change its name --> "hide")
    hide() {
      this.$emit("UserEditOK");
      this.resetUserData();
      this.$refs.userEditDialog.hide();
      
    },

    onDialogHide() {
      // required to be emitted
      // when QDialog emits "hide" event
      this.resetUserData();
      this.$emit("hide");
      this.$emit("UserEditOK");
    },

    onOKClick() {
      // on OK, it is REQUIRED to
      // emit "ok" event (with optional payload)
      // before hiding the QDialog
      if (this.op_type === "Update") {
        this.patchUserData();
      } else {
        this.createNewUser();
      }

      this.$emit("ok");

      // or with payload: this.$emit('ok', { ... })

      // then hiding dialog
      this.hide();
    },
    onCancelClick() {
      // we just need to hide dialog
      this.hide();
    },
  },
};
</script>

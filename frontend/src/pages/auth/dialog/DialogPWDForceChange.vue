<template>
  <q-dialog ref="userPWDForceDialog" @hide="onDialogHide">
    <q-card style="width: 700px; max-width: 85vw;">
      <q-card-section>
        <div class="text-h6">
          Force Change Password
        </div>
      </q-card-section>
      <div class="q-pa-md">
        <div class="q-gutter-x-lg q-pa-md row">
          <q-input
            filled
            v-model="udata.new_password"
            label="New Password"
            stack-label
          />
        </div>
      </div>      
      {{ udata }}
      <q-card-actions align="right">
        <q-btn color="primary" label="OK" @click="onOKClick" />
        <q-btn color="primary" label="Cancel" @click="onCancelClick" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import { PWDForceUpdate } from "src/api/auth";
export default {
  name: "ModalPwdForceChange",
  props: {
    user_id: {
      type: [Number, String],
      required: true,
    }
 
    // ...your custom props
  },
  data() {
    return {
      udata: {
        id: '',
        NewPassword:''
      },      
    };
  }, // END OF DATA
  methods: {
    resetUserData() {
      this.udata = {
        id: '',
        new_password:''
      };
    },
    patchPWD() {

      PWDForceUpdate(this.user_id, this.udata)
        .then((response) => {
          console.log(response);
          this.$q.notify({
          message: "Password successfully changed",
          position:'top',
          color:'green'
        })
        })
        .catch((error) => {
          console.log(error);
          this.$q.notify({
          message: "Password change failed",
          position:'top',
          color:'red'
        })
        });
    },
    // following method is REQUIRED
    // (don't change its name --> "show")
    show() {
      // console.log(this.user_id);
      // console.log(this.op_type === "Create");
      // console.log(this.localreadonlyFlag);
      this.udata.id = this.user_id
      this.$refs.userPWDForceDialog.show();
    },

    // following method is REQUIRED
    // (don't change its name --> "hide")
    hide() {
      this.$emit("UserEditOK");
      this.resetUserData();
      this.$refs.userPWDForceDialog.hide();
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
      this.patchPWD()

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

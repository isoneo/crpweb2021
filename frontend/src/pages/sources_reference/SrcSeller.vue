<template>
  <q-page class="q-pa-sm">
    <h4 class="text-center">Sources - Seller</h4>

    <div class="q-pa-md row justify-center">
      <q-table
        :dense="$q.screen.lt.md"
        title="Seller List"
        :rows="tbl_data"
        :columns="tbl_columns"
        :visible-columns="visible_tbl_columns"
        :loading="tbl_loading"
        row-key="ref_fund_list_id"
        v-model:pagination="tbl_pagination"
        :filter="tbl_filter"
        @request="Tblquery"
      >
        <template v-slot:top-right>
          <div class="q-pa-md q-gutter-sm row">
            <q-input
              debounce="350"
              v-model="tbl_filter"
              filled
              clearable
              dense
              color="green-8"
              placeholder="Search"
            >
              <template v-slot:append>
                <q-icon name="search" />
              </template>
            </q-input>
            <q-select
              v-model="visible_tbl_columns"
              multiple
              outlined
              dense
              options-dense
              :display-value="$q.lang.table.columns"
              emit-value
              map-options
              :options="tbl_columns"
              option-value="name"
              options-cover
              style="min-width: 150px"
            />
            <q-btn
              icon="fas fa-plus-circle"
              label="Add new record"
              @click="sw_dialog_src_fund"
            />
          </div>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<script>
import { reactive, toRefs, onMounted } from "vue";
import { useQuasar } from "quasar";

import { api_src_ref_seller_list } from "src/api/source_reference";
import DialogSrcFund from "src/pages/sources_reference/dialogs/DialogSrcFund";

export default {
  setup(props, context) {
    // Some Setup stuf
    const event = reactive({
      tbl_data: [],
      tbl_filter: "",
      tbl_columns: [
        {
          name: "seller_id",
          align: "center",
          label: "ID",
          field: "seller_id",
          sortable: true,
        },
        {
          name: "seller_name",
          align: "center",
          label: "Seller Name",
          field: "seller_name",
          sortable: true,
        },
        {
          name: "company",
          align: "center",
          label: "Company",
          field: "company",
          sortable: true,
        },
        {
          name: "main_contact_person_name",
          align: "center",
          label: "Main Contact",
          field: "main_contact_person_name",
          sortable: true,
        },
        {
          name: "address1",
          align: "center",
          label: "Address1",
          field: "address1",
          sortable: true,
        },
        {
          name: "address2",
          align: "center",
          label: "Address2",
          field: "address2",
          sortable: true,
        },
        {
          name: "city",
          align: "center",
          label: "City",
          field: "city",
          sortable: true,
        },
        {
          name: "state",
          align: "center",
          label: "State",
          field: "state",
          sortable: true,
        },
        {
          name: "zip_code",
          align: "center",
          label: "ZIP",
          field: "zip_code",
          sortable: true,
        },
        {
          name: "phone1",
          align: "center",
          label: "Phone1",
          field: "phone1",
          sortable: true,
        },
        {
          name: "phone2",
          align: "center",
          label: "Phone2",
          field: "phone2",
          sortable: true,
        },
        {
          name: "main_email",
          align: "center",
          label: "Email",
          field: "main_email",
          sortable: true,
        },
      ],
      visible_tbl_columns: [
        "seller_name",
        "main_conatct_person_name",
        "main_email",
        "phone1",
      ],
      total_row: 0,
      tbl_loading: false,
      tbl_pagination: {
        sortBy: "",
        descending: false,
        page: 1,
        rowsPerPage: 5,
        rowsNumber: 0,
      },
    });
    const $q = useQuasar();
    function sw_dialog_src_fund() {
      $q.dialog({
        component: DialogSrcFund,

        // props forwarded to your custom component
        componentProps: {
          text: "something",
          // ...more..props...
        },
      })
        .onOk(() => {
          console.log("OK");
          onTblDataLoad();
        })
        .onCancel(() => {
          console.log("Cancel");
        })
        .onDismiss(() => {
          console.log("Called on OK or Cancel");
        });
    }

    function onTblDataLoad(query) {
      // console.log(props)
      event.tbl_loading = !event.tbl_loading;
      console.log(query);
      api_src_ref_seller_list(query).then((response) => {
        console.log(response);
        event.tbl_data = response.data.results;
        event.tbl_pagination.rowsNumber = response.data.count;

        // event.total_row = response.data.count;
      });
      // if (typeof query !== "undefined") {
      //   event.tbl_pagination.page = query.page;
      //   event.tbl_pagination.rowsPerPage = query.page_size;
      //   event.tbl_pagination.sortBy = query.ordering;
      // }
      console.log(event.tbl_pagination);

      event.tbl_loading = !event.tbl_loading;
    }
    function Tblquery(props) {
      const { page, rowsPerPage, sortBy, descending } = props.pagination;
      const filter = props.filter;
      console.log(props);
      // var page = info.page
      // var page_size = info.pageSize
      var sort_txt;
      var cmb_txt = {};
      sort_txt = "";

      // Setting Sort parameters
      // if (info.sort.prop !== '' & typeof info.sort.prop !== 'undefined') {
      //   if (info.sort.order === 'descending') {
      //     sort_txt = '-' + info.sort.prop.split('.').join('__')
      //   } else {
      //     sort_txt = info.sort.prop.split('.').join('__')
      //   }
      // }
      // // Fxiing Page information only if filter
      // if (info.type === 'filter') {
      //   page = 1
      // }
      // cmb_txt['project_id'] = this.main_id
      if (filter !== "" && filter !== null) {
        console.log(filter);
        cmb_txt["search"] = filter;
      }
      cmb_txt["page"] = page;
      cmb_txt["page_size"] = rowsPerPage;

      event.tbl_pagination.page = page;
      event.tbl_pagination.rowsPerPage = rowsPerPage;
      event.tbl_pagination.sortBy = sortBy;
      if (descending === true) {
        cmb_txt["ordering"] = sortBy;
      } else {
        cmb_txt["ordering"] = "-" + sortBy;
      }

      event.tbl_pagination.descending = descending;

      onTblDataLoad(cmb_txt);
    }
    function check_tbl_update(props, data) {
      console.log(data);
      console.log(props);
      console.log(event.tbl_pagination);
      const { page, rowsPerPage, sortBy, descending } = props.pagination;
      console.log(page);
      console.log(rowsPerPage);
      console.log(sortBy);
      console.log(descending);
    }
    onMounted(() => {
      onTblDataLoad({ page_size: 5 });
      // check_tbl_update({
      //   pagination: event.tbl_pagination,
      //   filter: event.tbl_filter,
      // });
    });
    // Then return Stuff
    return {
      ...toRefs(event),
      onTblDataLoad,
      sw_dialog_src_fund,
      check_tbl_update,
      Tblquery,
    };
  },
};
</script>

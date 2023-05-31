<template>
  <div class="home">
    <el-row display="margin-top:10px">
        <el-input name="bookname" v-model="input_book_name" placeholder="请输入书名" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-input name="bookauthor" v-model="input_book_author" placeholder="请输入作者" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-button type="primary" @click="addBook()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
        <el-table :data="bookList" style="width: 100%" border>
          <el-table-column prop="id" label="编号" min-width="100">
            <template scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>
          <el-table-column prop="book_name" label="书名" min-width="100">
            <template scope="scope"> {{ scope.row.fields.book_name }} </template>
          </el-table-column>
          <el-table-column prop="book_name" label="作者" min-width="100">
            <template scope="scope"> {{ scope.row.fields.book_author }} </template>
          </el-table-column>
          <el-table-column prop="add_time" label="添加时间" min-width="100">
            <template scope="scope"> {{ scope.row.fields.create_time }} </template>
          </el-table-column>
          <el-table-column label="Operations">
            <template #default="scope">
            <el-button size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
        </el-table>
    </el-row>
    <el-pagination background layout="prev, pager, next" :total="1000"></el-pagination>
  </div>
</template>

<script>
export default {
  name: 'Book',
  data () {
    return {
      input_book_name: '',
      input_book_author: '',
      bookList: []
    }
  },
  mounted: function () {
    this.showBooks()
  },
  methods: {
    addBook () {
      this.$http.get('http://127.0.0.1:8000/books/add_book?book_name=' + this.input_book_name + '&book_author=' + this.input_book_author)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.showBooks()
          } else {
            this.$message.error('新增书籍失败，请重试')
            console.log(res['msg'])
          }
        })
    },
    showBooks () {
      this.$http.get('http://127.0.0.1:8000/books/show_books')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.bookList = res['list']
          } else {
            this.$message.error('查询书籍失败')
            console.log(res['msg'])
          }
        })
    }
  /* deleteBook(){
      console.log(this)
    }  */
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>

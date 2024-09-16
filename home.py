# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

# ini salam


def run():
    # [theme]
    # base="dark"
    st.set_page_config(
        page_title="Halloo",
        page_icon="👋",
    )

    st.write("# Selamat Datang .. 👋")

    st.sidebar.success("pilih menu di atas")
    # ini awalan penjelasan
    st.markdown(
        """
        Ini halaman khusus :blue[dashboard untuk menampilkan / _visualisasi_ data] sederhana, yang sebelumnya data tersebut sudah _cleaning_ secara ringkas 
        kemudian deploy dengan :blue[Streamlit], pembuatan projek ini dengan pemograman :blue[Python] dan :blue[Github] sebagai repository projek ini.
        
        👈 _Silahkan pilih menu di sidebar_ untuk mengaksesnya
        
        :red[Note] Jika akses menggunakan _mobile / handphone / gawai_
        
        _Menu_ dapat diakses dengan klik _button_ seperti (>) pada :blue[pojok kiri atas]

        ### Informasi
        - Website [streamlit.io](https://streamlit.io)
        - Repository Github [Projek Ini](https://github.com/rsbqr/Data-Analis-Projek.git)
        
        ### Penjelasan Singkat mengenai Data
        - [Bike Data Sharing](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

        Projek ini menggunakan data yang tersedia di website kaggle dan mencakup data pada tahun 2011 sampai 2012 
        yang tercatat pada sistem berbagi sepeda (Bike Data Sharing) Capital yang berisi informasi cuaca, musiman,
        jumlah sepeda sewaan per jam dan harian.
        """
    )


if __name__ == "__main__":
    run()

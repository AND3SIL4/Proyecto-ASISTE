import Footer from "components/navigation/Footer";
import Navbar from "components/navigation/Navbar";
import Layout from "hocs/layouts/Layout";
import { useEffect } from "react";
import { get_aprendices } from "redux/actions/aprendices";
import { connect } from "react-redux";

function Home({ get_aprendices, aprendices }) {
  useEffect(() => {
    window.scroll(0, 0);
    get_aprendices();
  }, []);
  return (
    <Layout>
      <Navbar/>
        <AperndicesInformation aprendices={aprendices} />
      <Footer />
    </Layout>
  );
}

function AperndicesInformation({ aprendices }) {
  return (
    <div>
      
      {aprendices &&
        aprendices.map((aprendiz) => (
          <div>
            <div>{ aprendiz.documento_aprendiz }</div>
            <div>{ aprendiz.nombres_aprendiz }</div>
            <div>{ aprendiz.user_details.email }</div>
          </div>
        ))}
    </div>
  );
}

const mapStateToProps = (state) => ({
  aprendices: state.aprendices.aprendices,
});
export default connect(mapStateToProps, {
  get_aprendices,
})(Home);

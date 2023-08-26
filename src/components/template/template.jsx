import React from 'react';
import { Layout, Menu } from 'antd';
import {
  UserOutlined,
  ShoppingCartOutlined,
  HomeOutlined,
} from '@ant-design/icons';
import './styles.css';
import { Link } from 'react-router-dom';

const { Header, Content, Footer } = Layout;

const MainTemplate = ({ children }) => {
  return (
    <Layout style={{ width: '100vw', height: '100vh' }}>
      <Header>
        <div className="logo" />
        <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
          <Menu.Item key="1" icon={<HomeOutlined />} >
            <Link to="/">Home</Link>
          </Menu.Item>
          <Menu.Item key="2" icon={<ShoppingCartOutlined />}>
            <Link to="/carrinho">Carrinho</Link>
          </Menu.Item>
          <Menu.Item key="3" icon={<UserOutlined />} style={{marginLeft: "auto"}}>
            <Link to="/usuario">Usuario</Link>
          </Menu.Item>
        </Menu>
      </Header>
      <Content>
        <div className="site-layout-content">
          {children}
        </div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        SinbaExpress ©{new Date().getFullYear()} Criado por SinbaGroup
      </Footer>
    </Layout>
  );
};

export default MainTemplate;

import Axios from 'axios';

const baseUrl = 'http://127.0.0.1:8000';

class ProdutoService {
    async getAllProdutos() {
        try {
            const response = await Axios.get(`${baseUrl}/produtos`);
            return response.data;
        } catch (error) {
            console.error('Erro ao buscar usuários:', error);
            throw error; // Você pode escolher relançar o erro ou tratá-lo de outra maneira.
        }
    }

    // Adicione outros métodos conforme necessário para realizar outras operações CRUD.
}

export default new ProdutoService();

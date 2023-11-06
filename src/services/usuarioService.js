import Axios from 'axios';

const baseUrl = 'http://127.0.0.1:8000';

class UsuarioService {
    async getAllUsuarios() {
        try {
            const response = await Axios.get(`${baseUrl}/clientes`);
            return response.data;
        } catch (error) {
            console.error('Erro ao buscar usuários:', error);
            throw error; // Você pode escolher relançar o erro ou tratá-lo de outra maneira.
        }
    }

    // Adicione outros métodos conforme necessário para realizar outras operações CRUD.
}

export default new UsuarioService();

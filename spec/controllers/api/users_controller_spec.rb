require 'rails_helper'

RSpec.describe Api::UsersController, type: :controller do
  describe 'GET #index' do
    it 'returns all users' do
      create_list :user, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe 'GET #show' do
    it 'returns detail for one user' do
      user = create :user

      get :show, params: { id: user.id }

      expect(json[:id]).to eq(user[:id])
      expect(json[:username]).to eq(user[:username])
    end
  end

  describe 'GET #create' do
    it 'creates a user' do
      post :create,
           params: { user: { username: 'aaronang' } }

      expect(json).to include(:id)
      expect(json[:username]).to eq('aaronang')
    end
  end
end

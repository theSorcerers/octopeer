require 'rails_helper'

RSpec.describe Api::RepositoriesController, type: :controller do
  describe "GET #index" do
    it "returns all repositories" do
      create_list :repository, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "returns detail for one repository" do
      repository = create :repository

      get :show, params: { id: repository.id }

      expect(json[:id]).to eq(repository.id)
      expect(json[:owner]).to eq(repository.owner)
      expect(json[:name]).to eq(repository.name)
      expect(json[:platform]).to eq(repository.platform)
    end
  end

  describe "GET #create" do
    it "creates a repository" do
      post :create,
           params: { repository: { owner: 'aaronang',
                                   name: 'octopeer',
                                   platform: 'bitbucket' } }

      expect(json).to include(:id)
      expect(json[:owner]).to eq('aaronang')
      expect(json[:name]).to eq('octopeer')
      expect(json[:platform]).to eq('bitbucket')
    end
  end
end

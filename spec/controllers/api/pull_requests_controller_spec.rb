require 'rails_helper'

RSpec.describe Api::PullRequestsController, type: :controller do
  describe "GET #index" do
    it "returns all pull requests" do
      create_list :pull_request, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "returns detail for one pull request" do
      pull_request = create :pull_request

      get :show, params: { id: pull_request.id }

      expect(json[:id]).to eq(pull_request.id)
      expect(json[:repository][:id]).to eq(pull_request.repository_id)
      expect(json[:pull_request_number]).to eq(pull_request.pull_request_number)
    end
  end

  describe "POST #create" do
    it "creates a pull request" do
      repository = create :repository

      post :create,
           params: { pull_request: { repository_id: repository.id,
                                     pull_request_number: 1 } }

      expect(json).to include(:id)
      expect(json[:repository][:id]).to eq(repository.id)
      expect(json[:pull_request_number]).to eq(1)
    end
  end
end

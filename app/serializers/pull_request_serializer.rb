class PullRequestSerializer < ActiveModel::Serializer
  attributes :id, :pull_request_number
  has_one :repository
end
